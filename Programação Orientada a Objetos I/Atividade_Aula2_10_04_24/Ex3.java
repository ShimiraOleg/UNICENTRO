public class Ex3{
	public static void main(String[] args){
		int lim = 0;
		System.out.print("\nSem Limite: \n");
		for(int i = 1; (i <= 100); i++)
		{
			if(i%2 != 0)
				System.out.print(i + " ");
		}
		
		System.out.print("\n\nCom Limite de 100: \n");
		for(int i = 0; (i <= 100) && (lim < 100); i++)
		{
			if(i%2 != 0)
			{	
				System.out.print(i + " ");
				lim += i;
			}
		}
	}
}