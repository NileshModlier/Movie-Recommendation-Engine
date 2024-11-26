<!DOCTYPE html>
<html>
<head>
    <title>Neovis.js Example</title>
    <script src="https://cdn.jsdelivr.net/npm/neovis.js/dist/neovis.js"></script>
</head>
<body>
    <div id="viz" style="width: 800px; height: 600px;"></div>
    <script>
        var config = {
            container_id: "viz",
            server_url: "bolt://localhost:7687",
            server_user: "neo4j",
            server_password: "password",
            labels: {
                "Movie": {
                    "caption": "title",
                    "size": "popularity"
                }
            },
            relationships: {
                "SIMILAR_TO": {
                    "thickness": "weight",
                    "caption": false
                }
            },
            initial_cypher: "MATCH (m:Movie)-[:SIMILAR_TO]-(rec:Movie) RETURN m, rec"
        };
        var viz = new Neovis.default(config);
        viz.render();
    </script>
</body>
</html>
