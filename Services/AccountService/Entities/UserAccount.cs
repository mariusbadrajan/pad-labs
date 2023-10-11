namespace AccountService.Entities;

public class UserAccount
{
    public Guid Id { get; set; }
    public Guid UserId { get; set; }
    public float Balance { get; set; }
}