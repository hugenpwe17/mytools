function [P_x] = my_interpx(X, Y, P_y)
    [Y, idx] = unique(Y);
    X = X(idx);
    P_x = interp1(Y,X,P_y,'linear');
end
