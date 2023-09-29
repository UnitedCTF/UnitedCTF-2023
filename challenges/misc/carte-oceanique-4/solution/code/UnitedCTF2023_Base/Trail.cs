namespace UnitedCTF2023_Base;

public class Trail
{
    public List<Node> Nodes { get; } = new();
    
    public Node Last { get; }

    public Trail(Node node)
    {
        Last = node;
        Nodes.Add(node);
    }

    public Trail(Node node, Trail trail) : this(node)
    {
        Nodes.AddRange(trail.Nodes);
    }

    public override string ToString()
    {
        var reverse = new List<Node>(Nodes);
        reverse.Reverse();
        var last = reverse.First();
        var format = last.Value.ToString();
        for (var i = 1; i < reverse.Count; i++)
        {
            format += $" {last.Next[reverse[i]]} {reverse[i].Value}";
            last = reverse[i];
        }

        return format;
    }
}