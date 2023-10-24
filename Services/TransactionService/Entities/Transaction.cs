namespace TransactionService.Entities;

public class Transaction
{
    public int Id { get; set; }
    public int UserId { get; set; }
    public int AccountId { get; set; }
    public string Type { get; set; } // ("Payment")
    public float Amount { get; set; }
    // public DateTimeOffset Timestamp { get; set; }
    public string Status { get; set; } // ("Completed")
}