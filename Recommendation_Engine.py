from neo4j import GraphDatabase

class MovieRecommendationEngine:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_recommendations(self, movie_title):
        with self.driver.session() as session:
            result = session.execute_read(self._find_and_return_recommendations, movie_title)
            return result

    @staticmethod
    def _find_and_return_recommendations(tx, movie_title):
        query = (
            "MATCH (m:Movie {title: $title})-[:SIMILAR_TO]-(rec:Movie) "
            "RETURN rec.title AS recommendation "
            "LIMIT 3"
        )
        result = tx.run(query, title=movie_title)
        return [record["recommendation"] for record in result]

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "Delhihouse$34"

    engine = MovieRecommendationEngine(uri, user, password)
    movie_title = input("Enter the movie title: ")
    recommendations = engine.get_recommendations(movie_title)
    print("Recommendations: ")
    for i, recommendation in enumerate(recommendations, 1):
        print(f"{i}. {recommendation}")
    engine.close()
