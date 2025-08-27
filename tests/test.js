function towerOfHanoi(n, source, destination, auxiliary) {
    if (n === 1) {
        console.log(`Chuyển đĩa 1 từ ${source} sang ${destination}`);
        return;
    }
    
    // Chuyển n-1 đĩa từ source sang auxiliary
    towerOfHanoi(n - 1, source, auxiliary, destination);
    
    // Chuyển đĩa lớn nhất
    console.log(`Chuyển đĩa ${n} từ ${source} sang ${destination}`);
    
    // Chuyển n-1 đĩa từ auxiliary sang destination
    towerOfHanoi(n - 1, auxiliary, destination, source);
}

// Tính số bước
function countMoves(n) {
    return Math.pow(2, n) - 1;
}

// Sử dụng
const n = 3;
console.log(`Giải bài toán Tháp Hà Nội với ${n} đĩa:`);
towerOfHanoi(n, 'A', 'C', 'B');
console.log(`Số bước tối thiểu: ${countMoves(n)}`);