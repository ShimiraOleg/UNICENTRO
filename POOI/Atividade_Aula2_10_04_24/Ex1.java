public class Ex1{
	public static void main(String[] args){
		int i = 10;
		
		System.out.print("\nExemplo While:\n");
		while(i <= 25){
			System.out.print(i + " ");
			i++;
		}
		i = 10;
		System.out.print("\n\nExemplo DoWhile:\n");
		do{
			System.out.print(i + " ");
			i++;
		} while(i <= 25);
		i = 25;
		System.out.print("\n\nExemplo For:\n");
		for(int j = 10; j <= i; j++)
		{
			System.out.print(j + " ");
		}
	}
}