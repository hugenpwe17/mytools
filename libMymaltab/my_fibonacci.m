function [F] = my_fibonacci(n)
% 斐波那契函数
% [第n位斐波那契数] = my_fibonacci(n)

% 初始化斐波那契数组
f = zeros(n,1);

% 初始化斐波那契的初值
f(1:2) = [0,1];

for i = 3:n
    f(i)=f(i-1)+f(i-2);
end
F = f(n);
end
