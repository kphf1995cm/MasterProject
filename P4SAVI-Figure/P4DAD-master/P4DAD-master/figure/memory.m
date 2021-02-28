hostnum= [10 200	400	600	800	1000]
mr2 = [180	3600	7200	10800	14400	18000]
mt2 = [340	6800	13600	20400	27200	34000]
ms2 = [520	10400	20800	31200	41600	52000]
mr4 = [360	7200	14400	21600	28800	36000]
mt4 = [540	10800	21600	32400	43200	54000]
ms4 = [900	18000	36000	54000	72000	90000]

figure(1);
plot(hostnum, mr2/1024,'-s','LineWidth',2, 'MarkerFaceColor','b')
hold on
plot(hostnum, mt2/1024,'-d','LineWidth',2, 'MarkerFaceColor','b')
plot(hostnum, ms2/1024,'-p','LineWidth',2, 'MarkerFaceColor','b')
plot(hostnum, mr4/1024,'-s','LineWidth',2, 'MarkerFaceColor','b')
plot(hostnum, mt4/1024,'-d','LineWidth',2, 'MarkerFaceColor','b')
plot(hostnum, ms4/1024,'-p','LineWidth',2, 'MarkerFaceColor','b')

axis([-100,1100,-10,100])
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
grid on
xlabel('Host Number');
ylabel('Memory Consumption (MB)');
legend('Register Memory ({\itn}=2)', 'MAT Memory ({\itn}=2)','Total ({\itn}=2)','Register Memory ({\itn}=4)','MAT Memory ({\itn}=4)','Total ({\itn}=4)');