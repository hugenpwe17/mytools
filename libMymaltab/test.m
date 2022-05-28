function test()
clear
clc
hfigure=figure;
haxes=axes;
hold on

plot((1:0.5:10)',sin(1:0.5:10)'*(1:10),'LineWidth',1);

hsel=plot(mean(haxes.XLim)*[1,1],haxes.YLim,... % 竖线
    'LineWidth',3,'ButtonDownFcn', @bdfcn);

opx=0;% 初始点的 x 坐标

    function bdfcn(hline,edata)
        % edata.Button=1 左键, 3 右键
        opx=edata.IntersectionPoint(1);
        hsel.Selected='on';
        hfigure.WindowButtonMotionFcn=@wbmfcn;
        hfigure.WindowButtonUpFcn=@wbufcn;
    end
    function wbmfcn(h,e)
        cp = haxes.CurrentPoint; % 鼠标位置
        hsel.XData=hsel.XData+cp(1,1)-opx;
        opx=cp(1,1);
    end
    function wbufcn(h,e)
        hfigure.WindowButtonMotionFcn='';
        hfigure.WindowButtonUpFcn='';
        hsel.Selected='off';
        % hsel.YData=haxes.YLim;
    end
end