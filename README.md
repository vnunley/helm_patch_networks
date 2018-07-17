# Explore Analyzing And Creating Helm Patches through Networks

### Main Ideas
- Randomly create helm patches (varying degree of deviation from init?) to rate
- Categorize and fitness-rate at least 100-200 'good' patches for training neural network 
- Train neural network to categorize and fitness-rate patch
  - Should we fitness rate even? If we do, possibly base it on the sound output? Probably a reach idea.
- Use a Generative Adversarial Network (GAN) for generating patches based on existing patches
  - For example, user would select either several patches they like or just broad labels of patches to be used as the basis for generation
- Use autoencoder/decoder network to simplify data vector representation
- 

### Libraries to use
- [GitHub - keras-team/keras: Deep Learning for humans](https://github.com/keras-team/keras)
  - For categorization neural network
- [SKIL Documentation](https://docs.skymind.ai/docs/welcome)
  - For GAN

### Tutorials
- [GAN: A Beginner’s Guide to Generative Adversarial Networks - Deeplearning4j: Open-source, Distributed Deep Learning for the JVM](https://deeplearning4j.org/generative-adversarial-network)
