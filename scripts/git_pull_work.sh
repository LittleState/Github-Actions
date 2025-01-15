#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

for dir in ./*/; do
    if [ -d "$dir/.git" ]; then
        echo -e "${YELLOW}Updating ${dir}${NC}"
	    (
		    cd "$dir" && git pull > /dev/null 2>&1
		    if [ $? -eq 0 ]; then
				echo -e "${GREEN}Update completed for ${dir}${NC}"
			else
				echo -e "${RED}Update Failed for ${dir}${NC}"
			fi
	    ) &
    else
	    echo "${RED}${dir} is not a git repository${NC}"
    fi
done

# 等待所有任务执行完成
wait
echo -e "${GREEN}All repositories updated.${NC}"
