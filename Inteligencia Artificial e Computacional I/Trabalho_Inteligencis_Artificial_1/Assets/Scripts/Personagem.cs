using UnityEngine;

public class Personagem : MonoBehaviour
{
    [SerializeField] private float velocidade = 5.0f;
    [SerializeField] private SceneController sc;
    private Rigidbody2D rb;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
           float moverX = Input.GetAxis("Horizontal");
           float moverY = Input.GetAxis("Vertical");

           rb.linearVelocity = new Vector2(moverX, moverY) * velocidade;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.layer == 7)
        {
            velocidade /= 2;
        }
    }
    
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.layer == 7)
        {
            velocidade *= 2;
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Inimigo"))
        {
            sc.GameOver();
        }
    }

}
