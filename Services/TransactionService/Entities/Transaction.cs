namespace TransactionService.Entities;

public class Transaction
{
    public Guid Id { get; set; }
    public Guid UserId { get; set; }
    public string Type { get; set; } // (e.g., "Payment," "Expense," or "Entity Payment")
    public float Amount { get; set; }
    public string Description { get; set; }
    public DateTime Timestamp { get; set; }
    public string Status { get; set; } // (e.g., "Completed," "Pending")
}