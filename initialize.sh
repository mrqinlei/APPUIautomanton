# vim initialize.sh
#!/bin/bash
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
echo $project_path
echo $project_name
echo "删除日志"
rm -rf $project_path/report/logs/*.txt
echo "删除截图"
rm -rf $project_path/report/pic/*.png
echo "删除xml文件"
rm -rf $project_path/report/xml/*.png
rm -rf $project_path/report/xml/*.txt
rm -rf $project_path/report/xml/*.json
