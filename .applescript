tell application "BetterTouchTool" to set dndEnabled to get_number_variable "SystemDoNotDisturbState"

if dndEnabled is 0 then
	set oportunitiesCount to do shell script "zsh /path/to/cumplo-tocuhbar-notification/run.sh"
	if oportunitiesCount > 0 then
		tell application "BetterTouchTool"
				return oportunitiesCount
		end tell
	else
		return ""
	end if
else
	return ""
end if
