public class QuickFindUF
{
	private int[] id;

	public QuickFindUF(int N)
	{
		id = new int[N];
		for (int i=0; i < N; i++)
			id[i] = i;
	}

	public boolean connected(int p, int q)
	{
		return id[p] == id[q];
	}

	public void union(int p, int q)
	{
		int p_val = id[p];
		for (int i=0; i<id.length; i++)
			if (id[i] == p_val)
				id[i] = id[q];
	}

	public void print_arr()
	{
		String str = "";
		for (int i=0; i<id.length;i++)
			str += id[i] + " ";
		System.out.println(str);
	}

	public static void main(String[] args)
	{
		// 3-1 9-6 8-3 6-0 7-9 7-2 
		QuickFindUF arr = new QuickFindUF(10);
		arr.print_arr();
		arr.union(3,1);
		arr.union(9,6);
		arr.union(8,3);
		arr.union(6,0);
		arr.union(7,9);
		arr.print_arr();
		arr.union(7,2);
		arr.print_arr();
		System.out.println("hahaha");

	}
	
}
// 0 1 2 1 4 5 0 0 1 0