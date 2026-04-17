# Brokex CFD Trading Implementation

class BrokexCFD:
    def __init__(self, asset, leverage):
        self.asset = asset
        self.leverage = leverage
        self.positions = []

    def open_position(self, size, direction):
        position = {"size": size, "direction": direction}
        self.positions.append(position)
        return position

    def close_position(self, position):
        if position in self.positions:
            self.positions.remove(position)
            return True
        return False

    def get_positions(self):
        return self.positions

# Example usage
if __name__ == '__main__':
    trading = BrokexCFD('BTC/USD', 10)
    trading.open_position(1, 'buy')
    print(trading.get_positions())
    trading.close_position(trading.positions[0])
    print(trading.get_positions())