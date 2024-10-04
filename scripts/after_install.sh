#!/usr/bin/bash

echo "Pull Finished"
sudo systemctl daemon-reload
if sudo systemctl restart nginx; then
  echo "Nginx restarted successfully"
else
  echo "Failed to restart Nginx" >&2
  sudo systemctl status nginx
fi