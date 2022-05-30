build:
	docker build . -t greynirseq_api
run:
	docker run -d --name=greynirseq -p 8080:8080 greynirseq_api
stop:
	docker container stop greynirseq
	docker container rm greynirseq
