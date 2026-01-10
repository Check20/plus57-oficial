// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

contract Plus57_V2 {
    string public name = "+57";
    string public symbol = "+57";
    uint8 public decimals = 18;
    uint256 public totalSupply = 7000000 * 10**18;

    mapping(address => uint256) private _balances;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        require(_balances[msg.sender] >= amount, "ERC20: balance low");
        _balances[msg.sender] -= amount;
        _balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
