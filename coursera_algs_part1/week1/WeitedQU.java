public class WeitedQU
{
	private int[] id;

	public WeitedQU(int N)
	{
		id = new int[N];
		for (int i=0; i < N; i++)
			id[i] = i;
	}

	public boolean connected(int p, int q)
	{
		return root(p) == root(q);
	}

	public int root(int i)
	{
		while (i != id[i])
		{
			id[i] = id[id[i]];
			i = id[i];
		}
		return i;
	}

	public void union(int p, int q)
	{
		int i = root(p);
		int j = root(q);
		id[i] = j;
	}

	public void print_arr()
	{
		String str = "";
		for (int i=0; i<this.id.length;i++)
			str += id[i] + " ";
		System.out.println(str);
	}

	public static void main(String[] args)
	{
		// 3-1 9-6 8-3 6-0 7-9 7-2 
		WeitedQU arr = new WeitedQU(10);
		arr.print_arr();
		arr.union(5,1);arr.print_arr();
		arr.union(5,9);arr.print_arr();
		arr.union(5,4);arr.print_arr();
		arr.union(2,3);arr.print_arr();
		arr.union(7,1);arr.print_arr();
		arr.union(0,6);arr.print_arr();
		arr.union(3,0);arr.print_arr();
		arr.union(9,3);arr.print_arr();
		arr.union(8,0);arr.print_arr();
		arr.print_arr();
		System.out.println("hahaha");

	}
	
}
// 0 1 2 1 4 5 0 0 1 0