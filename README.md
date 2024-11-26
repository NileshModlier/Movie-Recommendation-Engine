Adding performance metrics is a great idea to evaluate and improve the recommendation engine. Here’s an updated version of the README file with a section for performance metrics:

---

# Movie Recommendation Engine using GraphRAG

## Overview
This project implements a movie recommendation engine using the GraphRAG architecture and Neo4j. The engine recommends similar movies based on the movie a user has watched. For example, if a user watches "3 Idiots", the engine will recommend three similar movies.

## Features
- **Graph Database**: Utilizes Neo4j to store and query movie data.
- **GraphRAG Architecture**: Combines knowledge graphs and retrieval-augmented generation for enhanced recommendations.
- **Interactive Visualization**: Visualize the movie graph using Neovis.js.

## Dataset
The dataset used in this project is sourced from Kaggle. It contains information about 10,000 Bollywood movies, including titles, genres, actors, directors, and more.

## Installation

### Prerequisites
- Python 3.x
- Neo4j (Community Edition)
- Neo4j Python Driver
- Neovis.js

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MovieRecommendationEngine.git
   cd MovieRecommendationEngine
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Neo4j**:
   - Download and install Neo4j from Neo4j Download Center.
   - Start the Neo4j server and open the Neo4j Browser.

4. **Load Dataset into Neo4j**:
   - Use the provided script to load the dataset into Neo4j.
   ```bash
   python load_data.py
   ```

## Usage

### Running the Recommendation Engine
1. **Start the Recommendation Engine**:
   ```bash
   python recommendation_engine.py
   ```

2. **Get Recommendations**:
   - The script will prompt you to enter a movie title.
   - It will then return three similar movie recommendations.

### Examples of Usage
- **Example 1**:
  ```bash
  Enter the movie title: 3 Idiots
  Recommendations: 
  1. Taare Zameen Par
  2. PK
  3. Munna Bhai M.B.B.S.
  ```

- **Example 2**:
  ```bash
  Enter the movie title: Dangal
  Recommendations: 
  1. Sultan
  2. Chak De! India
  3. Bhaag Milkha Bhaag
  ```

### Visualization
1. **Open the Visualization**:
   - Open the `index.html` file in a web browser to visualize the movie graph.

## Project Structure
```
MovieRecommendationEngine/
│
├── input_database/
│   └── bollywood_dataset.csv
│
├── code/
│   ├── load_data.py
│   └── recommendation_engine.py
│
├── model_architecture/
│   └── architecture_slide.pptx
│
├── demo_video/
│   └── demo.mp4
│
└── index.html
```

## Model Architecture
The recommendation engine uses the GraphRAG architecture, which combines knowledge graphs and retrieval-augmented generation. The architecture leverages Neo4j for storing and querying movie data and uses a Python script to generate recommendations.

## Demo
A demo video explaining the approach, code, and output is available in the `demo_video` folder. Watch the demo video here.

## Performance Metrics
To evaluate the performance of the recommendation engine, the following metrics can be used:
- **Precision**: The proportion of recommended movies that are relevant.
- **Recall**: The proportion of relevant movies that are recommended.
- **F1 Score**: The harmonic mean of precision and recall.
- **Mean Average Precision (MAP)**: The mean of the average precision scores for each query.
- **Mean Reciprocal Rank (MRR)**: The average of the reciprocal ranks of the first relevant recommendation.
- **Hit Rate**: The proportion of users for whom at least one of the top-N recommendations is relevant.

### Example Evaluation
```python
from sklearn.metrics import precision_score, recall_score, f1_score

# Example data
true_relevant = [1, 0, 1, 1, 0]  # Ground truth relevance
predicted_relevant = [1, 0, 1, 0, 0]  # Predicted relevance

# Calculate metrics
precision = precision_score(true_relevant, predicted_relevant)
recall = recall_score(true_relevant, predicted_relevant)
f1 = f1_score(true_relevant, predicted_relevant)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
```

## Future Improvements
- **Enhanced Recommendation Algorithm**: Incorporate more sophisticated algorithms such as collaborative filtering or content-based filtering to improve recommendation accuracy.
- **User Profiles**: Implement user profiles to provide personalized recommendations based on user preferences and watch history.
- **Scalability**: Optimize the system to handle larger datasets and more complex queries efficiently.
- **Additional Data Sources**: Integrate additional data sources such as user ratings, reviews, and social media interactions to enrich the recommendation engine.
- **Real-time Recommendations**: Develop a real-time recommendation system that updates recommendations as the user interacts with the platform.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
- Kaggle for providing the dataset.
- Neo4j for the graph database.
- Neovis.js for the visualization library.

---
