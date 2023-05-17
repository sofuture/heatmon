.PHONY: all
all: run

.PHONY: run
run:
	python3 heatmon.py

.PHONY: install
install:
	@echo "sudo cp heatmon.service /lib/systemd/system/heatmon.service"
	@echo "sudo systemctl enable heatmon.service"
	@echo "sudo systemctl start heatmon.service"

.PHONY: deps
deps:
	sudo apt install git python3-pip
	sudo pip install w1thermsensor prometheus_client
	sudo sed -i "s/#Storage=auto/Storage=volatile/g" /etc/systemd/journald.conf
	@echo "DD_API_KEY=xxx DD_SITE="us3.datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
	sudo cp heatmon.conf /etc/datadog-agent/conf.d/openmetrics.d/heatmon.conf

