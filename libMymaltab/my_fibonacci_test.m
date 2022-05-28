%% Output the first n Fibonacci numbers
% the number of outputs
n = 10;

fi_array = zeros(1,n);

for i = 1:n
    fi_array(i) = my_fibonacci(i);
end

disp(['前', num2str(n), '位的斐波那契数如下:']);
disp(fi_array);
