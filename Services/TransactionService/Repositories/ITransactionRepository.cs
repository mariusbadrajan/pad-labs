using TransactionService.Entities;

namespace TransactionService.Repositories;

public interface ITransactionRepository
{
    public Task<List<Transaction>> GetAllTransactionsAsync();
    public Task<List<Transaction>> GetAllTransactionsByUserIdAsync(Guid userId);
    public Task<Transaction> GetTransactionByIdAsync(Guid id);
    public Task<Transaction> AddTransactionAsync(Transaction account);
    public Task<Transaction> UpdateTransactionAsync(Transaction account);
    public Task DeleteTransactionByIdAsync(Guid id);
}