function [y_interp] = my_lagrange(x_init, y_init, x_interp)
% 拉格朗日插值
% x_init:   初始x值
% y_init:   初始y值
% x_interp: 插值点
% y_interp: 插值

% 初始化插值数组
y_interp = x_interp;

% 计算插值
for i = 1 : length(x_interp)
    z = x_interp(i);
    s = 0.0;
    for k = 1:length(x_init)
        p = 1.0;
        for j = 1 : length(x_init)
            if j ~= k
                p = p * (z - x_init(j)) / (x_init(k) - x_init(j));
            end
        end
        s = p * y_init(k) + s;
    end
    y_interp(i) = s;
end