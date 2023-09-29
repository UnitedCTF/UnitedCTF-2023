namespace UnitedCTF2023_Base;

public static class NodeLoader
{
    public static Node Load(string filename)
    {
        var stream = File.OpenRead(filename);
        var reader = new StreamReader(stream);
        var numberOfNode = int.Parse(reader.ReadLine());
        var n = new Node[numberOfNode];
        for (var i = 0; i < numberOfNode; i++)
        {
            var value = long.Parse(reader.ReadLine());
            n[i] = new Node
            {
                Value = value
            };
        }

        var links = reader.ReadToEnd().Split("\n");
        foreach (var link in links)
        {
            var from = int.Parse(link.Trim().Split(" ")[0]);
            var to = int.Parse(link.Trim().Split(" ")[1]);
            var sign = link.Trim().Split(" ")[2];
            n[from].Next.Add(n[to], sign);
        }

        return n[0];
    }
}