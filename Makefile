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
