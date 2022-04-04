docker container stop greynirseq
docker container rm greynirseq
docker build . -t glaciersg/greynirseq_api:v1.0.0
docker run -d --name=greynirseq -p 8080:8080 glaciersg/greynirseq_api:v1.0.0
