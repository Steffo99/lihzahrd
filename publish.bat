git commit -am "publish: %1"
git push && poetry build && poetry publish && hub release create "%1" -m "Lihzahrd %1"