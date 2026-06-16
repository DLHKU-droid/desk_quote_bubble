on run
	set isRunning to do shell script "pgrep -f lc_cat.py | head -1 || true"
	if isRunning is not "" then
		display notification "桌面语录已在运行中" with title "桌面语录" subtitle "如需重启请先关闭气泡右上角 ×"
	else
		do shell script "/Users/dailing/miniconda3/bin/python3 /Users/dailing/lc_cat.py > /tmp/lc_cat.log 2>&1 &"
		delay 1
		display notification "桌面语录已启动" with title "桌面语录"
	end if
end run
