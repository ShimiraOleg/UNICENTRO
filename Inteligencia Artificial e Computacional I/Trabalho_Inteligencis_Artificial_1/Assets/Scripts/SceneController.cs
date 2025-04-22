using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneController : MonoBehaviour
{
    [SerializeField] private GameObject cena;
    [SerializeField] private GameObject ui;

    public void GameOver(){
        Debug.Log("morreu");
        cena.SetActive(false);
        ui.SetActive(true);
    }

    public void MenuStart(){
        Debug.Log("Beuh");
        SceneManager.LoadScene("Cena Principal");
    }

    public void Restart(){
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void Fechar(){
        #if UNITY_STANDALONE
            Application.Quit();
        #endif
        #if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
        #endif
    }

}
