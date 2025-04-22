using System.Collections.Generic;
using UnityEngine;

public class EnemyAI : MonoBehaviour
{
    [Header("Configurações de Movimento")]
    [SerializeField] private float velocidadeMovimento = 3f;
    [SerializeField] private float distanciaProximoWaypoint = 0.3f;
    [SerializeField] private float pathUpdateRate = 0.5f;
    
    [Header("Configurações de Visão")]
    [SerializeField] private float alcanceDeVisao = 7f;
    [SerializeField] private float anguloDeVisao = 120f;
    [SerializeField] private LayerMask camadaObstaculo;
    [SerializeField] private bool desenharVisionGizmos = true;
    [SerializeField] private Sprite[] iconesEstado;
    [SerializeField] private GameObject iconeEstado;
    
    [Header("Comportamento Idle")]
    [SerializeField] private float raioPatrulhandoIdle = 5f;
    [SerializeField] private float minTempoIdle = 2f;
    [SerializeField] private float maxTempoIdle = 5f;
    [SerializeField] private Vector3 posicaoHome;
    
    [Header("Comportamento Investigação")]
    [SerializeField] private float duracaoDeInvestigacao = 5f;
    [SerializeField] private float raioDeInvestigacao = 3f;
    [SerializeField] private int contadorDePontoDeInvetigacao = 3;
    
    [Header("Referencias da Cena")]
    [SerializeField] private Transform target; // Player
    [SerializeField] private AStarPathfinding pathfinder;

    // Variaveis de Caminho
    private List<Node> caminhoAtual;
    private int waypointAtual = 0;
    private float caminhoUpdateTimer;
    
    // Variaveis de Estado
    private enum estadoInimigo { Idle, Patrulhando, Perseguindo, Investigando }
    private estadoInimigo estadoAtual = estadoInimigo.Idle;
    private Vector3 idleTargetPosition;
    private float timerDeEstado;
    
    // Variaveis de Investigação
    private Vector3 ultimaLocalizaoPlayer;
    private readonly List<Vector3> pontosDeInvestigacao = new();
    private int pontoDeInvestigacaoAtual = 0;
    
    // Variavel de Visão
    private bool isJogadorVisivel = false;

    private void Start()
    {
        if (target == null)
            target = GameObject.FindGameObjectWithTag("Player").transform;
        
        if (pathfinder == null)
            pathfinder = FindFirstObjectByType<AStarPathfinding>();
            
        StartEstadoIdle();
    }

    private void Update()
    {
        isJogadorVisivel = ChecarVisao();
        
        // Update current state
        UpdateEstadoInimigo();
        
        // Handle behavior based on state
        switch (estadoAtual)
        {
            case estadoInimigo.Idle:
                iconeEstado.GetComponent<SpriteRenderer>().sprite = iconesEstado[0]; 
                HandleEstadoIdle();
                break;
                
            case estadoInimigo.Patrulhando:
                iconeEstado.GetComponent<SpriteRenderer>().sprite = iconesEstado[1]; 
                HandleEstadoPatrulha();
                break;
                
            case estadoInimigo.Perseguindo:
                iconeEstado.GetComponent<SpriteRenderer>().sprite = iconesEstado[2]; 
                HandleEstadoPerseguicao();
                break;
                
            case estadoInimigo.Investigando:
                iconeEstado.GetComponent<SpriteRenderer>().sprite = iconesEstado[3];
                HandleEstadoInvestigacao();
                break;
        }
        
        SeguirCaminho();
    }
    
    private bool ChecarVisao()
    {
        if (target == null)
            return false;
            
        Vector3 directionToTarget = target.position - transform.position;
        float distanceToTarget = directionToTarget.magnitude;
        
        if (distanceToTarget > alcanceDeVisao)
            return false;
            
        float angle = Vector3.Angle(transform.right, directionToTarget.normalized);
        if (angle > anguloDeVisao / 2)
            return false;
            
        RaycastHit2D hit = Physics2D.Raycast(
            transform.position,
            directionToTarget.normalized,
            distanceToTarget,
            camadaObstaculo
        );
        
        if (hit.collider == null)
        {
            ultimaLocalizaoPlayer = target.position;
            return true;
        }
        
        return false;
    }
    
    private void UpdateEstadoInimigo()
    {
        if (isJogadorVisivel && estadoAtual != estadoInimigo.Perseguindo)
        {
            TransicaoDeEstado(estadoInimigo.Perseguindo);
            return;
        }
        
        switch (estadoAtual)
        {
            case estadoInimigo.Idle:
                if (timerDeEstado <= 0)
                {
                    TransicaoDeEstado(estadoInimigo.Patrulhando);
                }
                break;
                
            case estadoInimigo.Patrulhando:
                if (caminhoAtual == null || waypointAtual >= caminhoAtual.Count)
                {
                    TransicaoDeEstado(estadoInimigo.Idle);
                }
                break;
                
            case estadoInimigo.Perseguindo:
                if (!isJogadorVisivel)
                {
                    TransicaoDeEstado(estadoInimigo.Investigando);
                }
                break;
                
            case estadoInimigo.Investigando:
                if (timerDeEstado <= 0 || (pontoDeInvestigacaoAtual >= pontosDeInvestigacao.Count && caminhoAtual == null))
                {
                    TransicaoDeEstado(estadoInimigo.Idle);
                }
                break;
        }
    }
    
    private void TransicaoDeEstado(estadoInimigo newState)
    {
        switch (estadoAtual)
        {
            case estadoInimigo.Investigando:
                pontosDeInvestigacao.Clear();
                break;
        }
        
        estadoAtual = newState;
        
        switch (newState)
        {
            case estadoInimigo.Idle:
                Debug.Log("Inimigo: Inicial Estado Idle");
                StartEstadoIdle();
                break;
                
            case estadoInimigo.Patrulhando:
                Debug.Log("Inimigo: Inicial Estado Patrulha");
                SetAlvoPatrulha();
                break;
                
            case estadoInimigo.Perseguindo:
                Debug.Log("Inimigo: Inicial Estado Perseguição - Player Visto!");
                caminhoUpdateTimer = pathUpdateRate;
                break;
                
            case estadoInimigo.Investigando:
                Debug.Log("Inimigo: Inicial Estado Investigação- Player Ultima Vez Visto em " + ultimaLocalizaoPlayer);
                posicaoHome = ultimaLocalizaoPlayer;
                StartInvestigacao();
                break;
        }
    }
    
    private void HandleEstadoIdle()
    {
        timerDeEstado -= Time.deltaTime;        
    }
    
    private void StartEstadoIdle()
    {
        timerDeEstado = Random.Range(minTempoIdle, maxTempoIdle);
        caminhoAtual = null;
    }
    
    private void HandleEstadoPatrulha()
    {
        caminhoUpdateTimer += Time.deltaTime;
        if (caminhoUpdateTimer >= pathUpdateRate)
        {
            UpdateCaminho(idleTargetPosition);
            caminhoUpdateTimer = 0f;
        }
    }
    
    private void SetAlvoPatrulha()
    {
        Vector2 randomDirection = Random.insideUnitCircle * raioPatrulhandoIdle;
        idleTargetPosition = posicaoHome + new Vector3(randomDirection.x, randomDirection.y, 0);
        
        UpdateCaminho(idleTargetPosition);
    }
    
    private void HandleEstadoPerseguicao()
    {
        caminhoUpdateTimer += Time.deltaTime;
        if (caminhoUpdateTimer >= pathUpdateRate / 2) 
        {
            if (isJogadorVisivel && target != null)
            {
                UpdateCaminho(target.position);
            }
            caminhoUpdateTimer = 0f;
        }
    }
    
    private void StartInvestigacao()
    {
        timerDeEstado = duracaoDeInvestigacao;
        
        GeneratePontosDeInvestigacao();
        pontoDeInvestigacaoAtual = 0;
        
        UpdateCaminho(ultimaLocalizaoPlayer);
    }
    
    private void GeneratePontosDeInvestigacao()
    {
        pontosDeInvestigacao.Clear();
        pontosDeInvestigacao.Add(ultimaLocalizaoPlayer);
        
        for (int i = 0; i < contadorDePontoDeInvetigacao - 1; i++)
        {
            float angle = i * (360f / (contadorDePontoDeInvetigacao - 1));
            Vector3 direction = Quaternion.Euler(0, 0, angle) * Vector3.right;
            Vector3 point = ultimaLocalizaoPlayer + direction * raioDeInvestigacao;
            
            pontosDeInvestigacao.Add(point);
        }
    }
    
    private void HandleEstadoInvestigacao()
    {
        timerDeEstado -= Time.deltaTime;
        
        if (caminhoAtual == null || waypointAtual >= caminhoAtual.Count)
        {
            pontoDeInvestigacaoAtual++;
            
            if (pontoDeInvestigacaoAtual < pontosDeInvestigacao.Count)
            {
                UpdateCaminho(pontosDeInvestigacao[pontoDeInvestigacaoAtual]);
                Debug.Log("Inimigo: Investigando ponto " + pontoDeInvestigacaoAtual);
            }
        }
        
        caminhoUpdateTimer += Time.deltaTime;
        if (caminhoUpdateTimer >= pathUpdateRate)
        {
            if (pontoDeInvestigacaoAtual < pontosDeInvestigacao.Count)
            {
                UpdateCaminho(pontosDeInvestigacao[pontoDeInvestigacaoAtual]);
            }
            caminhoUpdateTimer = 0f;
        }
    }
    
    private void UpdateCaminho(Vector3 targetPosition)
    {
        if (pathfinder != null)
        {
            caminhoAtual = pathfinder.FindPath(transform.position, targetPosition);
            waypointAtual = 0;
        }
    }
    
    private void SeguirCaminho()
    {
        if (caminhoAtual == null || waypointAtual >= caminhoAtual.Count)
            return;
        
        Vector3 direction = (caminhoAtual[waypointAtual].worldPosition - transform.position).normalized;
        transform.Translate(direction * velocidadeMovimento * Time.deltaTime);
        
        float distance = Vector2.Distance(transform.position, caminhoAtual[waypointAtual].worldPosition);
        if (distance < distanciaProximoWaypoint)
        {
            waypointAtual++;
        }
    }
    
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.layer == 7)
        {
            velocidadeMovimento /= 2;
        }
    }
    
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.layer == 7)
        {
            velocidadeMovimento *= 2;
        }
    }
    
    // Visualize the path and vision in the Scene view
    private void OnDrawGizmos()
    {
        // Draw current path
        if (caminhoAtual != null)
        {
            Gizmos.color = Color.blue;
            for (int i = waypointAtual; i < caminhoAtual.Count; i++)
            {
                Gizmos.DrawSphere(caminhoAtual[i].worldPosition, 0.2f);
                if (i < caminhoAtual.Count - 1)
                {
                    Gizmos.DrawLine(caminhoAtual[i].worldPosition, caminhoAtual[i + 1].worldPosition);
                }
            }
        }
        
        // Draw vision cone
        if (desenharVisionGizmos)
        {
            // Vision cone color: red when seeing player, yellow otherwise
            Gizmos.color = isJogadorVisivel ? Color.red : Color.yellow;
            
            // Draw vision range as arc
            Vector3 forward = transform.right; // Assuming enemy faces right as default
            Vector3 leftBoundary = Quaternion.Euler(0, 0, anguloDeVisao / 2) * forward;
            Vector3 rightBoundary = Quaternion.Euler(0, 0, -anguloDeVisao / 2) * forward;
            
            // Draw vision boundaries
            Gizmos.DrawLine(transform.position, transform.position + leftBoundary * alcanceDeVisao);
            Gizmos.DrawLine(transform.position, transform.position + rightBoundary * alcanceDeVisao);
            
            // Draw arc segments
            int segments = 20;
            Vector3 prevPoint = transform.position + rightBoundary * alcanceDeVisao;
            
            for (int i = 1; i <= segments; i++)
            {
                float angle = -anguloDeVisao / 2 + anguloDeVisao * i / segments;
                Vector3 direction = Quaternion.Euler(0, 0, angle) * forward;
                Vector3 point = transform.position + direction * alcanceDeVisao;
                
                Gizmos.DrawLine(prevPoint, point);
                prevPoint = point;
            }
            
            // Draw home position and patrol radius
            Gizmos.color = Color.cyan;
            Gizmos.DrawWireSphere(posicaoHome, raioPatrulhandoIdle);
            
            // Draw last known player position and investigation area
            if (ultimaLocalizaoPlayer != Vector3.zero)
            {
                // Draw last known position
                Gizmos.color = Color.magenta;
                Gizmos.DrawWireSphere(ultimaLocalizaoPlayer, 0.5f);
                
                // Draw investigation radius if in investigation state
                if (estadoAtual == estadoInimigo.Investigando)
                {
                    Gizmos.DrawWireSphere(ultimaLocalizaoPlayer, raioDeInvestigacao);
                    
                    // Draw all investigation points
                    Gizmos.color = Color.red;
                    foreach (Vector3 point in pontosDeInvestigacao)
                    {
                        Gizmos.DrawSphere(point, 0.3f);
                    }
                    
                    // Highlight current investigation point
                    if (pontoDeInvestigacaoAtual < pontosDeInvestigacao.Count)
                    {
                        Gizmos.color = Color.green;
                        Gizmos.DrawSphere(pontosDeInvestigacao[pontoDeInvestigacaoAtual], 0.4f);
                    }
                }
            }
        }
    }
}