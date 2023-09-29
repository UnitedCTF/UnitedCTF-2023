namespace UnitedCTF2023_Base;

public class Node
{
    public Dictionary<Node, string> Next { get; set; } = new();
    public long Value { get; set; }
}