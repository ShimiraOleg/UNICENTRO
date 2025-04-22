using System;
using System.Collections.Generic;
using UnityEngine;

public class AStarPathfinding : MonoBehaviour
{
    // Grid settings
    [SerializeField] private Vector2Int tamanhoDoGrid = new(38, 24);
    [SerializeField] private float raioDoNode = 0.25f;
    [SerializeField] private LayerMask camadaDeObstaculo;    
    // Visualization
    [SerializeField] private bool visualizeGrid = true;
    [SerializeField] private TerrainType[] terrainTypes;

    [Serializable]
    public class TerrainType
    {
        public string name; 
        public LayerMask terrainMask;
        public int terrainCost; 
        public Color terrainColor = Color.white; 
    }
    
    // Pathfinding components
    private Node[,] grid;
    private float diametroDoNode;
    private Vector3 gridWorldSize;
    
    private void Awake()
    {
        diametroDoNode = raioDoNode * 2;
        gridWorldSize = new Vector3(tamanhoDoGrid.x * diametroDoNode, tamanhoDoGrid.y * diametroDoNode, 0);
        CriarGrid();
    }
    
    private void CriarGrid()
    {
        grid = new Node[tamanhoDoGrid.x, tamanhoDoGrid.y];
        Vector3 worldBottomLeft = transform.position - Vector3.right * gridWorldSize.x / 2 - Vector3.up * gridWorldSize.y / 2;
        
        for (int x = 0; x < tamanhoDoGrid.x; x++)
        {
            for (int y = 0; y < tamanhoDoGrid.y; y++)
            {
                Vector3 worldPoint = worldBottomLeft + Vector3.right * (x * diametroDoNode + raioDoNode) + Vector3.up * (y * diametroDoNode + raioDoNode);
                
                bool walkable = !Physics2D.OverlapCircle(worldPoint, raioDoNode, camadaDeObstaculo);
                int terrainCost = 0;
                
                foreach (TerrainType terrain in terrainTypes)
                {
                    if (Physics2D.OverlapCircle(worldPoint, raioDoNode, terrain.terrainMask))
                    {
                        terrainCost = terrain.terrainCost;
                        break; 
                    }
                }
                grid[x, y] = new Node(walkable, worldPoint, x, y, terrainCost);
            }
        }
    }
    
    public List<Node> GetVizinhos(Node node)
    {
        List<Node> vizinhos = new List<Node>();
        
        for (int x = -1; x <= 1; x++)
        {
            for (int y = -1; y <= 1; y++)
            {
                if (x == 0 && y == 0)
                    continue;
                    
                int checkX = node.gridX + x;
                int checkY = node.gridY + y;
                
                if (checkX >= 0 && checkX < tamanhoDoGrid.x && checkY >= 0 && checkY < tamanhoDoGrid.y)
                {
                    vizinhos.Add(grid[checkX, checkY]);
                }
            }
        }
        return vizinhos;
    }
    
    public Node NodeFromWorldPoint(Vector3 worldPosition)
    {
        float percentX = (worldPosition.x + gridWorldSize.x / 2) / gridWorldSize.x;
        float percentY = (worldPosition.y + gridWorldSize.y / 2) / gridWorldSize.y;
        
        percentX = Mathf.Clamp01(percentX);
        percentY = Mathf.Clamp01(percentY);
        
        int x = Mathf.RoundToInt((tamanhoDoGrid.x - 1) * percentX);
        int y = Mathf.RoundToInt((tamanhoDoGrid.y - 1) * percentY);
        
        return grid[x, y];
    }
    
    public List<Node> FindPath(Vector3 startPos, Vector3 targetPos)
    {
        Node startNode = NodeFromWorldPoint(startPos);
        Node targetNode = NodeFromWorldPoint(targetPos);
        
        List<Node> openSet = new List<Node>();
        HashSet<Node> closedSet = new HashSet<Node>();
        openSet.Add(startNode);
        
        while (openSet.Count > 0)
        {
            Node currentNode = openSet[0];
            
            for (int i = 1; i < openSet.Count; i++)
            {
                if (openSet[i].fCost < currentNode.fCost || 
                    (openSet[i].fCost == currentNode.fCost && openSet[i].hCost < currentNode.hCost))
                {
                    currentNode = openSet[i];
                }
            }
            
            openSet.Remove(currentNode);
            closedSet.Add(currentNode);
            
            if (currentNode == targetNode)
            {
                return RetracePath(startNode, targetNode);
            }
            
            foreach (Node neighbor in GetVizinhos(currentNode))
            {
                if (!neighbor.walkable || closedSet.Contains(neighbor))
                    continue;
                    
                int newMovementCostToNeighbor = currentNode.gCost + GetDistance(currentNode, neighbor) + neighbor.terrainCost;
                if (newMovementCostToNeighbor < neighbor.gCost || !openSet.Contains(neighbor))
                {
                    neighbor.gCost = newMovementCostToNeighbor;
                    neighbor.hCost = GetDistance(neighbor, targetNode);
                    neighbor.parent = currentNode;
                    
                    if (!openSet.Contains(neighbor))
                        openSet.Add(neighbor);
                }
            }
        }
        
        return null;
    }
    
    private List<Node> RetracePath(Node startNode, Node endNode)
    {
        List<Node> path = new List<Node>();
        Node currentNode = endNode;
        
        while (currentNode != startNode)
        {
            path.Add(currentNode);
            currentNode = currentNode.parent;
        }
        
        path.Reverse();
        return path;
    }
    
    private int GetDistance(Node nodeA, Node nodeB)
    {
        int distX = Mathf.Abs(nodeA.gridX - nodeB.gridX);
        int distY = Mathf.Abs(nodeA.gridY - nodeB.gridY);
        
        if (distX > distY)
            return 14 * distY + 10 * (distX - distY);
        return 14 * distX + 10 * (distY - distX);
    }
    
    private void OnDrawGizmos()
    {
        if (!visualizeGrid || grid == null)
            return;
            
        foreach (Node node in grid)
        {
            // Default color for unwalkable nodes
            if (!node.walkable)
            {
                Gizmos.color = Color.red;
            }
            else
            {
                // Find the matching terrain type for visualization
                bool terrainFound = false;
                foreach (TerrainType terrain in terrainTypes)
                {
                    if (terrain.terrainCost == node.terrainCost)
                    {
                        Gizmos.color = terrain.terrainColor;
                        terrainFound = true;
                        break;
                    }
                }
                
                // If no matching terrain, use gradient based on cost
                if (!terrainFound)
                {
                    if (node.terrainCost > 0) // Penalty
                    {
                        // Red gradient for penalties
                        float intensity = Mathf.Clamp01(node.terrainCost / 100f);
                        Gizmos.color = Color.Lerp(Color.white, Color.red, intensity);
                    }
                    else if (node.terrainCost < 0) // Reward
                    {
                        // Green gradient for rewards
                        float intensity = Mathf.Clamp01(-node.terrainCost / 50f);
                        Gizmos.color = Color.Lerp(Color.white, Color.green, intensity);
                    }
                    else // No cost
                    {
                        Gizmos.color = Color.white;
                    }
                }
            }
            
            // Draw the node
            Gizmos.DrawWireCube(node.worldPosition, Vector3.one * diametroDoNode * 0.9f);
        }
    }
}

public class Node
{
    public bool walkable;
    public Vector3 worldPosition;
    public int gridX;
    public int gridY;
    public int terrainCost = 0;
    
    public int gCost;
    public int hCost;
    public Node parent;
    
    public int fCost { get { return gCost + hCost; } }
    
    public Node(bool _walkable, Vector3 _worldPos, int _gridX, int _gridY, int _terrainCost = 0)
    {
        walkable = _walkable;
        worldPosition = _worldPos;
        gridX = _gridX;
        gridY = _gridY;
        terrainCost = _terrainCost;
    }

    internal int GetTerrainType()
    {
        return terrainCost;
    }
}
