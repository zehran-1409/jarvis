# Jarvis V0.5 - Text-Based Assistant
# Your first real program, Emperor Zehran

print("=" * 40)
print("J.A.R.V.I.S. V0.5 - At Your Service, Boss.")
print("=" * 40)

# Step 1: Get the boss's name
name = input("\nWhat should I call you, boss?")
print(f"\nWelcome, {name}. I am ready to assist.")

while True:
    print("\n" + "-" * 40)
    print("What you like me to do?")
    print("1. Calculate trade profit/loss")
    print("2. Check my mood")
    print("3. Exit")
    choice = input("Enter you choice (1/2/3): ")

    if choice == "1":
        # Trade profit/loss calculator
        print("\n--- Trade Calculator ---")
        stock = input("Sotck name: ")
        buy_price = float(input("Buy price per share (₹): "))
        sell_price = float(input("Sell price per share (₹): "))
        quantity = int(input("Number of shhares: "))

        total_cost = buy_price * quantity
        total_revenue = sell_price * quantity
        profit_loss = total_revenue - total_cost

        print(f"\nTrade Summary for {stock}:")
        print(f"Total Cost: ₹{total_cost:.2f}")
        print(f"Total Revenue: ₹{total_revenue:.2f}")
        if profit_loss >= 0:
            print(f"✅ Profit: ₹{profit_loss:.2f}")
        else:
            print(f"❌ Loss: ₹{-profit_loss:.2f}")

        #Journal the trade
        journal_entry = f"{stock} | Buy: {buy_price} | Sell: {sell_price} | Qty: {quantity} | P/L: {profit_loss:.2f}"
        with open("trade_journal.txt", "a") as f:
            f.write(journal_entry + "\n")
        print("Trade logged to journal.")

    elif choice == "2":
        # Simple mood check
        mood = input("\nHow are you feeling right now, boss? ")
        if "good" in mood.lower() or " great" in mood.lower() or "happy" in mood.lower():
            print("Excellent. Let's channel that energy into building the empire.")
        elif "low" in mood.lower() or "sad" in mood.lower() or "tired" in mood.lower():
            print("I understand, Emperor. Even the greatest machines need a reset. Remember your Tahajjud. You are not alone.")
        else:
            print("Noted. I'm tracking all states. You are in control.")

    elif choice == "3":
        print(f"\nGoodbye, {name}. The empire awaits your next command.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
    
