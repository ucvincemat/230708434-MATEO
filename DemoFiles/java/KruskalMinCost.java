import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class KruskalMinCost {
	public static void main(String[] args) {
		Scanner acceptInput = new Scanner(System.in);
		ArrayList<Edge> edges = new ArrayList<>();
		String divider = "--------------------------------";
		boolean mainLoop = true;
		
		// Intro
		System.out.println();
		System.out.println("     KRUSKAL'S MINIMUM COST CALCULATOR v1.a");
		System.out.println("           \"The easiest for last!\"");
		System.out.println("=========X=====<=============>======X==========");
		System.out.println();
		System.out.println("USAGE:\nWhen adding a new vertex relation, use the (v,w,c) format.\n" +
						   "You can stack them in a single line too! Just make sure to follow the format!\n\n" +
						   "Note: 'v' and 'w' represents the vertices and 'c' represents the cost of the edge connecting them.\n\n" +
						   "Example:\n" +
						   "(K,B,3) (K,F,3) (B,F,3) (B,G,4) (B,D,4) (D,G,4) (F,A,5) (F,G,5)\n");
		System.out.println(divider);
		
		// Initialize minCost
		int minCost = 0;
		
		// Loop
		while (mainLoop) {
			System.out.println("< Minimum cost: " + minCost + " >");
			System.out.println(divider);
			
			System.out.println( "| (1) Add new vertex relations\n" +
									"|\n" +
									"| (S) Start over\n" +
									"| (X) Quit Program\n" +
									".................................");
			
			System.out.print("Command: ");
			String command = acceptInput.nextLine().toUpperCase().trim();
			char action = (command.isEmpty()) ? '0' : command.charAt(0);
			System.out.println(divider);
			
			switch (action) {
				case '1':
					System.out.print("Add (v,w,c) -> ");
					String input = acceptInput.nextLine().trim();
					
					// Input catch (using regular expressions :D)
					String inputPattern = "\\(\\s*[^,)]+\\s*,\\s*[^,)]+\\s*,\\s*-?\\d+\\s*\\)(?:\\s*\\(\\s*[^,)]+\\s*,\\s*[^,)]+\\s*,\\s*-?\\d+\\s*\\))*";
					
					if (!input.matches(inputPattern)) {
						System.out.println("\n[!] WRONG! You follow the format of (v,w,c)!");
						break;
					}
					
					input = input.substring(1, input.length() - 1); // Remove outer parenthesis
					
					String[] edgeInputs = input.split("\\)\\s*\\("); // Split input by parenthesis

					// Parse the input and add the edges
					for (String edgeInput : edgeInputs) {
						String[] values = edgeInput.split("\\s*,\\s*"); // Split values by comma
						String src = values[0];
						String dest = values[1];
						int cost = Integer.parseInt(values[2]);
						if (cost != 0) // If the value is non-zero, then there exist a connection i.e. 0 = no edge
							edges.add(new Edge(src, dest, cost));
					}
					break;
				case 'S':
					System.out.println("[@] Resetting...");	
                    edges.clear();
                    break;
				case 'X':
					mainLoop = false;
					break;
				default:
					System.out.println("[!] Invalid command.");
			
			}
			System.out.println(divider);
			minCost = kruskalMST(edges);
		}
		// Outro
		acceptInput.close();
		System.out.println("Terminating program... Goodbye! o/");
		terminate();
	}
	
	// Class to represent an edge in the graph
	static class Edge implements Comparable<Edge> {
		String src, dest;
		int cost;

		// Constructor to initialize an edge
		public Edge(String src, String dest, int cost) {
			this.src = src;
			this.dest = dest;
			this.cost = cost;
		}

		// Method to compare edges based on their costs
		public int compareTo(Edge compareEdge) {
			return this.cost - compareEdge.cost;
		}
	}

	// Class to represent a subset for union-find algorithm
	static class Subset {
		int parent, rank;
	}

	// Method to find the subset of a particular element using path compression
	static int find(Subset subsets[], int i) {
		if (subsets[i].parent != i)
			subsets[i].parent = find(subsets, subsets[i].parent);

		return subsets[i].parent;
	}

	// Method to perform union of two subsets based on rank
	static void union(Subset subsets[], int x, int y) {
		int xroot = find(subsets, x);
		int yroot = find(subsets, y);

		if (subsets[xroot].rank < subsets[yroot].rank)
			subsets[xroot].parent = yroot;
		else if (subsets[xroot].rank > subsets[yroot].rank)
			subsets[yroot].parent = xroot;
		else {
			subsets[yroot].parent = xroot;
			subsets[xroot].rank++;
		}
	}

	// Method to find the minimum spanning tree using Kruskal's algorithm
	static int kruskalMST(ArrayList<Edge> edges) {
		int totalCost = 0;
		ArrayList<Edge> result = new ArrayList<>();

		// Sort the edges based on their costs
		Collections.sort(edges);

		// Create a mapping of vertices to unique IDs
		HashMap<String, Integer> vertexIds = new HashMap<>();
		int id = 0;
		for (Edge edge : edges) {
			if (!vertexIds.containsKey(edge.src))
				vertexIds.put(edge.src, id++);
			if (!vertexIds.containsKey(edge.dest))
				vertexIds.put(edge.dest, id++);
		}

		// Determine the number of vertices in the graph
		int V = vertexIds.size();

		// Initialize subsets for each vertex
		Subset subsets[] = new Subset[V];
		for (int i = 0; i < V; ++i)
			subsets[i] = new Subset();

		for (int v = 0; v < V; ++v) {
			// Initialize parent and rank for each subset
			subsets[v].parent = v;
			subsets[v].rank = 0;
		}

		// Perform Kruskal's algorithm
		int e = 0;
		for (Edge edge : edges) {
			int srcId = vertexIds.get(edge.src);
			int destId = vertexIds.get(edge.dest);

			int x = find(subsets, srcId);
			int y = find(subsets, destId);

			// Check if including this edge creates a cycle
			if (x != y) {
				result.add(edge);
				totalCost += edge.cost;
				union(subsets, x, y);
				e++;
			}
		}

		// If everything doesn't connect properly, print error message
		if (e < V - 1) {
			System.out.println("[!] No spanning tree");
			return 0;
		}

		return totalCost;
	}
	
	// im so funny
	private static void terminate() {
		System.out.println( "             _____ _____ _  _   \n" +
						"           / ____/ ____| || |  \n" +
						"          | |   | |    | || |_ \n" +
						"          | |   | |    |__   _|\n" +
						"          | |___| |____   | |  \n" +
						"           \\_____\\_____|  |_|  \n" +
						"                        \n" +
						"    And that concludes the final Lab!\n" +
						"        Best of luck in the exam!");
	}
}