import java.util.ArrayList;
import java.util.ListIterator;

public class DefinirNomes {
    public static void main(String[] args) {
        ArrayList<String> arrayNomes = new ArrayList<String>();
        arrayNomes.add("Antunes");
        arrayNomes.add("Paulo");
        arrayNomes.add("João");

        ListIterator<String> listItr = arrayNomes.listIterator();
        while (listItr.hasNext())
        {
            listItr.next();
            if(!(listItr.hasNext()))
            {
                while (listItr.hasPrevious())
                {
                    System.out.println(listItr.previous());
                }
                break;
            }
        }
    }
}
