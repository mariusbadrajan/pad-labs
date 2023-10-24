using TransactionService.Entities;

namespace TransactionService.Repositories;

public interface IRepository
{
    public Task<List<Transaction>> GetAllUserTransactionsAsync(int userId);
    public Task<List<Transaction>> GetAllAccountTransactionsAsync(int accountId);
    public Task<Transaction> GetTransactionByIdAsync(int id);
    public Task<Transaction> AddTransactionAsync(Transaction account);
    public Task<Transaction> UpdateTransactionAsync(Transaction account);
    public Task DeleteTransactionByIdAsync(int id);
}