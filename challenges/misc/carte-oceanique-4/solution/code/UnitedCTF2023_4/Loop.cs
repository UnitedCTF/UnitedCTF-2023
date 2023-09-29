using UnitedCTF2023_Base;

namespace UnitedCTF2023_4;

public class Loop
{
    public Node EntryPoint { get; private init; }
    public bool IsDivergent { get; private init; }
    
    public Loop(Node entryPoint, bool isDivergent)
    {
        EntryPoint = entryPoint;
        IsDivergent = isDivergent;
    }

}