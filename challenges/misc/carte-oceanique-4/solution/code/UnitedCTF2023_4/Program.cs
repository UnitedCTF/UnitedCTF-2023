// See https://aka.ms/new-console-template for more information

using UnitedCTF2023_4;
using UnitedCTF2023_Base;

var node = NodeLoader.Load("nodes.txt");

var loops = new Dictionary<Node, Loop>();
var nodes = new Stack<Node>();

Recursion(node, nodes, loops);

var mainLoop = loops.First(loop => !loop.Value.IsDivergent);
var mainLoopEntryPointScores = new List<long>();

var results = new List<(Trail, long)>();
var currentIt = new HashSet<(Trail, long)>
{
    (new Trail(node), node.Value)
};

var toIt = new HashSet<(Trail, long)>();

var hasLooped = false;

while (currentIt.Any() && !hasLooped)
{
    foreach (var (item1, oldScore) in currentIt)
    {
        if (item1.Last == mainLoop.Key)
        {
            if (mainLoopEntryPointScores.Contains(oldScore))
            {
                hasLooped = true;
                break;
            }

            mainLoopEntryPointScores.Add(oldScore);
        }
        
        
        if (item1.Last.Next.Any())
        {
            foreach (var next in item1.Last.Next)
            {
                var newScore = oldScore;
                switch (next.Value)
                {
                    case "+":
                        try
                        {
                            checked
                            {
                                newScore += next.Key.Value;
                            }
                            toIt.Add((new Trail(next.Key, item1), newScore));
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
                            toIt.Add((new Trail(next.Key, item1), newScore));
                        } catch (OverflowException) {}
                        break;
                    case "*":
                        try
                        {
                            checked
                            {
                                newScore *= next.Key.Value;
                            }
                            toIt.Add((new Trail(next.Key, item1), newScore));
                        } catch (OverflowException) {}
                        break;
                    case "/":
                        if (next.Key.Value != 0)
                        {
                            toIt.Add((new Trail(next.Key, item1), oldScore / next.Key.Value));
                        }
                        break;
                    case "%":
                        toIt.Add((new Trail(next.Key, item1), oldScore % next.Key.Value));
                        break;
                }
            }
        }
        else
        {
            results.Add((item1, oldScore));
        }
    }

    currentIt = toIt;
    toIt = new HashSet<(Trail, long)>();
}

Console.Write(results.MaxBy(t => t.Item2));
return;

void Recursion(Node next, Stack<Node> nodePile, Dictionary<Node, Loop> loopsDictionary)
{
    if (nodePile.Contains(next))
    {
        var tmp = new Stack<Node>();
        var last = next;
        var isDivergent = true;
        while (nodePile.Peek() != next)
        {
            var current = nodePile.Pop();
            if (current.Next[last] == "%")
            {
                isDivergent = false;
            }
            
            last = current;
            tmp.Push(current);
        }
        tmp.Push(nodePile.Pop());

        var loop = new Loop(next, isDivergent);
        loopsDictionary.Add(next, loop);
        while (tmp.Any())
        {
            nodePile.Push(tmp.Pop());
        }
    }
    else
    {
        nodePile.Push(next);
        foreach (var (n, value) in next.Next)
        {
            Recursion(n, nodePile, loopsDictionary);
        }

        nodePile.Pop();
        next.Next = next.Next
            .Where(kpv =>
            {
                if (loopsDictionary.TryGetValue(kpv.Key, out var l))
                {
                    return !l.IsDivergent;
                }

                return true;
            })
            .ToDictionary(kpv => kpv.Key, kpv => kpv.Value);
    }
}
