// See https://aka.ms/new-console-template for more information

using UnitedCTF2023_Base;

var node = NodeLoader.Load("nodes.txt");
var results = new List<(Trail, long)>();
var currentIt = new HashSet<(Trail, long)>
{
    (new Trail(node), node.Value)
};

var toIt = new HashSet<(Trail, long)>();

var used = new HashSet<Node>();

while (currentIt.Any())
{
    foreach (var currentNode in currentIt)
    {
        used.Add(currentNode.Item1.Last);
        if (currentNode.Item1.Last.Next.Any())
        {
            foreach (var next in currentNode.Item1.Last.Next)
            {
                if (!used.Contains(next.Key))
                {
                    used.Add(next.Key);
                    long oldScore = currentNode.Item2;
                    long newScore = oldScore;
                    switch (next.Value)
                    {
                        case "+":
                            try
                            {
                                checked
                                {
                                    newScore += next.Key.Value;
                                }
                                toIt.Add((new Trail(next.Key, currentNode.Item1), newScore));
                            }
                            catch (OverflowException)
                            {
                                
                            }
                            break;
                        case "-":
                            try
                            {
                                checked
                                {
                                    newScore -= next.Key.Value;
                                }
                                toIt.Add((new Trail(next.Key, currentNode.Item1), newScore));
                            } catch (OverflowException) {}
                            break;
                        case "*":
                            try
                            {
                                checked
                                {
                                    newScore *= next.Key.Value;
                                }
                                toIt.Add((new Trail(next.Key, currentNode.Item1), newScore));
                            } catch (OverflowException) {}
                            break;
                        case "/":
                            if (next.Key.Value != 0)
                            {
                                toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 / next.Key.Value));
                            }
                            break;
                        case "%":
                            toIt.Add((new Trail(next.Key, currentNode.Item1), currentNode.Item2 % next.Key.Value));
                            break;
                    }
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
