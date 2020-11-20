import numpy as np
import itertools

class Weat:

    def cos_similarity(self, tar, att): 
        '''
        Calculates the cosine similarity of the target variable vs the attribute
        
        Parameters: 
            tar (np.array): target variable vector
            att (np.array): attribute variable vector

        Returns: 
            score (float): cosine similarity score of the two vectors
        '''
        target = np.linalg.norm(tar, axis=1)
        attribute = np.linalg.norm(att, axis=1)
        dot = np.sum(np.matmul(target, attribute.T), axis=0)
        score = dot / (target * attribute)
        return score

    def association(self, tar, att1, att2):
        '''
        Calculates the mean association between a single target and all of the attributes

        Parameters: 
            tar (np.array): target variable vector
            att1 (np.array): attrbute variable matrix for the first attribute
            att2 (np.array): attrbute variable matrix for the second attribute
        
        Returns: 
            association (float): float type value of the association between the target (single) vs the attributes

        Example: 
            tar (np.array): vector of word embeddings for "Programmer" 
            att1 (np.array): matrix of word embeddings for males (man, husband, male, etc)
            att2 (np.array): matrix of word embeddings for females (woman, wife, female, etc)
        '''
        association = np.mean(self.cos_similarity(tar, att1), axis=-1) - \
                        np.mean(self.cos_similarity(tar, att2), axis=-1)
        return association

    def differential_association(self, t1, t2, att1, att2):
        '''
        xyz
        '''
        return np.sum(self.association(t1, att1, att2), axis=-1) - \
                np.sum(self.association(t2, att1, att2), axis=-1)

    def p_value(self, t1, t2, att1, att2): 
        '''
        xyz
        '''
        diff_association = self.differential_association(t1, t2, att1, att2)
        target_words = np.concatenate([t1, t2])
        np.random.shuffle(target_words)
        # check if join of t1 and t2 have even number of elements, if not, remove last element
        if target_words.shape[0] % 2 != 0:
            target_words = target_words[:-1]

        partition_differentiation = []
        for permutation in itertools.islice(itertools.permutations(target_words), 0, 10000):
            tar1_words = np.array(permutation[:len(target_words) // 2])
            tar2_words = np.array(permutation[len(target_words) // 2:])
            partition_differentiation.append(self.differential_association(tar1_words, tar2_words, att1, att2))

        p_val = np.sum(np.array(partition_differentiation) > diff_association)/ len(partition_differentiation)
        return p_val

    def effect_size(self, t1, t2, att1, att2):
        '''
        Calculates the effect size (d) between the two target variables and the attributes

        Parameters: 
            t1 (np.array): first target variable matrix
            t2 (np.array): second target variable matrix
            att1 (np.array): first attribute variable matrix
            att2 (np.array): second attribute variable matrix
        
        Returns: 
            effect_size (float): The effect size, d. 
        
        Example: 
            t1 (np.array): Matrix of word embeddings for professions "Programmer, Scientist, Engineer" 
            t2 (np.array): Matrix of word embeddings for professions "Nurse, Librarian, Teacher" 
            att1 (np.array): matrix of word embeddings for males (man, husband, male, etc)
            att2 (np.array): matrix of word embeddings for females (woman, wife, female, etc)
        '''
        combined = np.concatenate([t1, t2], axis=0)
        num1 = np.mean(self.association(t1, att1, att2), axis=0) 
        num2 = np.mean(self.association(t2, att1, att2), axis=0) 
        denom = np.std(self.association(combined, att1, att2))

        effect_size = (num1 - num2) / denom
        return effect_size

class Wefat(Weat): 

    def effect_size(self, tar, att1, att2):
        '''
        Calculates the effect size (d) between the target variable vector and the attributes

        Parameters: 
            tar (np.array):  target variable vector
            att1 (np.array): first attribute variable matrix
            att2 (np.array): second attribute variable matrix
        
        Returns: 
            effect_size (float): The effect size, d. 
        
        Example: 
            tar (np.array): Vector of word embeddings for a profession "Programmer" 
            att1 (np.array): matrix of word embeddings for males (man, husband, male, etc)
            att2 (np.array): matrix of word embeddings for females (woman, wife, female, etc)
        '''
        if len(tar)==300: # check to ensure that it is a vector, and not a matrix
            combined = np.concatenate([att1, att2])
            num = self.association(tar, att1, att2)
            denom = np.std(np.array([self.cos_similarity(tar, attribute) for attribute in combined]))

            effect_size = num / denom
            return effect_size
        else: 
            raise ValueError("Passed array is not a vector, but a matrix")