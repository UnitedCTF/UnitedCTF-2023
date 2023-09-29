// See https://aka.ms/new-console-template for more information

using UnitedCTF2023_Base;

var node = NodeLoader.Load("nodes.txt");
var results = new List<(Trail, long)>();
var currentIt = new HashSet<(Trail, long)>
{
    (new Trail(node), node.Value)
};

var toIt = new HashSet<(Trail, long)>();

while (currentIt.Any())
{
    foreach (var currentNode in currentIt)
    {
        if (currentNode.Item1.Last.Next.Any())
        {
            foreach (var next in currentNode.Item1.Last.Next)
            {
                switch (next.Value)
                {
                    case "+":
                        toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 + next.Key.Value));
                        break;
                    case "-":
                        toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 - next.Key.Value));
                        break;
                    case "*":
                        toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 * next.Key.Value));
                        break;
                    case "/":
                        toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 / next.Key.Value));
                        break;
                    case "%":
                        toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 % next.Key.Value));
                        break;
                }
            }
        }
        else
        {
            results.Add(currentNode);
        }
    }

    currentIt = toIt;
    toIt = new HashSet<(Trail, long)>();
}

Console.Write(results.MaxBy(t => t.Item2));