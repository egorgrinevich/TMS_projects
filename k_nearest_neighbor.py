{"payload":{"allShortcutsEnabled":true,"fileTree":{"homeworks/assignment01_knn":{"items":[{"name":"README.md","path":"homeworks/assignment01_knn/README.md","contentType":"file"},{"name":"k_nearest_neighbor.py","path":"homeworks/assignment01_knn/k_nearest_neighbor.py","contentType":"file"},{"name":"knn_assignment_0_01.ipynb","path":"homeworks/assignment01_knn/knn_assignment_0_01.ipynb","contentType":"file"}],"totalCount":3},"homeworks":{"items":[{"name":"assignment01_knn","path":"homeworks/assignment01_knn","contentType":"directory"},{"name":"assignment02_laplace","path":"homeworks/assignment02_laplace","contentType":"directory"}],"totalCount":2},"":{"items":[{"name":"homeworks","path":"homeworks","contentType":"directory"},{"name":"step01_intro","path":"step01_intro","contentType":"directory"},{"name":"step02_linear_regression","path":"step02_linear_regression","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"prerequisites.md","path":"prerequisites.md","contentType":"file"}],"totalCount":6}},"fileTreeProcessingTime":5.377022999999999,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":168725504,"defaultBranch":"master","name":"ml-course","ownerLogin":"girafe-ai","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2019-02-01T19:20:39.000+03:00","ownerAvatar":"https://avatars.githubusercontent.com/u/66535367?v=4","public":true,"private":false,"isOrgOwned":true},"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"23f_yandex_ml_trainings","listCacheKey":"v0:1698951803.0","canEdit":true,"refType":"branch","currentOid":"ce4de5edfdc21ee0fca1e8ab2079221a51005faa"},"path":"homeworks/assignment01_knn/k_nearest_neighbor.py","currentUser":{"id":132013325,"login":"egorgrinevich","userEmail":"egor.grinevich@gmail.com"},"blob":{"rawLines":["import numpy as np","\"\"\"","Credits: the original code belongs to Stanford CS231n course assignment1. Source link: http://cs231n.github.io/assignments2019/assignment1/","\"\"\"","","class KNearestNeighbor:","    \"\"\" a kNN classifier with L2 distance \"\"\"","","    def __init__(self):","        pass","","    def fit(self, X, y):","        \"\"\"","        Train the classifier. For k-nearest neighbors this is just","        memorizing the training data.","","        Inputs:","        - X: A numpy array of shape (num_train, D) containing the training data","          consisting of num_train samples each of dimension D.","        - y: A numpy array of shape (N,) containing the training labels, where","             y[i] is the label for X[i].","        \"\"\"","        self.X_train = X","        self.y_train = y","","    def predict(self, X, k=1, num_loops=0):","        \"\"\"","        Predict labels for test data using this classifier.","","        Inputs:","        - X: A numpy array of shape (num_test, D) containing test data consisting","             of num_test samples each of dimension D.","        - k: The number of nearest neighbors that vote for the predicted labels.","        - num_loops: Determines which implementation to use to compute distances","          between training points and testing points.","","        Returns:","        - y: A numpy array of shape (num_test,) containing predicted labels for the","          test data, where y[i] is the predicted label for the test point X[i].","        \"\"\"","        if num_loops == 0:","            dists = self.compute_distances_no_loops(X)","        elif num_loops == 1:","            dists = self.compute_distances_one_loop(X)","        elif num_loops == 2:","            dists = self.compute_distances_two_loops(X)","        else:","            raise ValueError('Invalid value %d for num_loops' % num_loops)","","        return self.predict_labels(dists, k=k)","","    def compute_distances_two_loops(self, X):","        \"\"\"","        Compute the distance between each test point in X and each training point","        in self.X_train using a nested loop over both the training data and the","        test data.","","        Inputs:","        - X: A numpy array of shape (num_test, D) containing test data.","","        Returns:","        - dists: A numpy array of shape (num_test, num_train) where dists[i, j]","          is the Euclidean distance between the ith test point and the jth training","          point.","        \"\"\"","        num_test = X.shape[0]","        num_train = self.X_train.shape[0]","        dists = np.zeros((num_test, num_train))","        for i in range(num_test):","            for j in range(num_train):","                #####################################################################","                # TODO:                                                             #","                # Compute the l2 distance between the ith test point and the jth    #","                # training point, and store the result in dists[i, j]. You should   #","                # not use a loop over dimension, nor use np.linalg.norm().          #","                #####################################################################","                # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","                # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","        return dists","","    def compute_distances_one_loop(self, X):","        \"\"\"","        Compute the distance between each test point in X and each training point","        in self.X_train using a single loop over the test data.","","        Input / Output: Same as compute_distances_two_loops","        \"\"\"","        num_test = X.shape[0]","        num_train = self.X_train.shape[0]","        dists = np.zeros((num_test, num_train))","        for i in range(num_test):","            #######################################################################","            # TODO:                                                               #","            # Compute the l2 distance between the ith test point and all training #","            # points, and store the result in dists[i, :].                        #","            # Do not use np.linalg.norm().                                        #","            #######################################################################","            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","        return dists","","    def compute_distances_no_loops(self, X):","        \"\"\"","        Compute the distance between each test point in X and each training point","        in self.X_train using no explicit loops.","","        Input / Output: Same as compute_distances_two_loops","        \"\"\"","        num_test = X.shape[0]","        num_train = self.X_train.shape[0]","        dists = np.zeros((num_test, num_train))","        #########################################################################","        # TODO:                                                                 #","        # Compute the l2 distance between all test points and all training      #","        # points without using any explicit loops, and store the result in      #","        # dists.                                                                #","        #                                                                       #","        # You should implement this function using only basic array operations; #","        # in particular you should not use functions from scipy,                #","        # nor use np.linalg.norm().                                             #","        #                                                                       #","        # HINT: Try to formulate the l2 distance using matrix multiplication    #","        #       and two broadcast sums.                                         #","        #########################################################################","        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","        return dists","","    def predict_labels(self, dists, k=1):","        \"\"\"","        Given a matrix of distances between test points and training points,","        predict a label for each test point.","","        Inputs:","        - dists: A numpy array of shape (num_test, num_train) where dists[i, j]","          gives the distance betwen the ith test point and the jth training point.","","        Returns:","        - y: A numpy array of shape (num_test,) containing predicted labels for the","          test data, where y[i] is the predicted label for the test point X[i].","        \"\"\"","        num_test = dists.shape[0]","        y_pred = np.zeros(num_test)","        for i in range(num_test):","            # A list of length k storing the labels of the k nearest neighbors to","            # the ith test point.","            #########################################################################","            # TODO:                                                                 #","            # Use the distance matrix to find the k nearest neighbors of the ith    #","            # testing point, and use self.y_train to find the labels of these       #","            # neighbors. Store these labels in closest_y.                           #","            # Hint: Look up the function numpy.argsort.                             #","            #########################################################################","            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","            #########################################################################","            # TODO:                                                                 #","            # Now that you have found the labels of the k nearest neighbors, you    #","            # need to find the most common label in the list closest_y of labels.   #","            # Store this label in y_pred[i]. Break ties by choosing the smaller     #","            # label.                                                                #","            #########################################################################","            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","","            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****","","        return y_pred"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-k"},{"start":16,"end":18,"cssClass":"pl-s1"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":139,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":22,"cssClass":"pl-v"}],[{"start":4,"end":45,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-v"},{"start":21,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":66,"cssClass":"pl-s"}],[{"start":0,"end":37,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":62,"cssClass":"pl-s"}],[{"start":0,"end":78,"cssClass":"pl-s"}],[{"start":0,"end":40,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-v"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-v"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":30,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":59,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":81,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":80,"cssClass":"pl-s"}],[{"start":0,"end":80,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":83,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":51,"cssClass":"pl-en"},{"start":52,"end":53,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":51,"cssClass":"pl-en"},{"start":52,"end":53,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":52,"cssClass":"pl-en"},{"start":53,"end":54,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":61,"cssClass":"pl-s"},{"start":62,"end":63,"cssClass":"pl-c1"},{"start":64,"end":73,"cssClass":"pl-s1"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":34,"cssClass":"pl-en"},{"start":35,"end":40,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":35,"cssClass":"pl-en"},{"start":36,"end":40,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-v"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":81,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":18,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":71,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":83,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-v"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":32,"cssClass":"pl-v"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":36,"end":45,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":31,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":36,"cssClass":"pl-s1"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":85,"cssClass":"pl-c"}],[{"start":16,"end":79,"cssClass":"pl-c"}],[],[{"start":16,"end":77,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":20,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":34,"cssClass":"pl-en"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-v"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":81,"cssClass":"pl-s"}],[{"start":0,"end":63,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":59,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-v"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":32,"cssClass":"pl-v"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":36,"end":45,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":31,"cssClass":"pl-s1"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":83,"cssClass":"pl-c"}],[{"start":12,"end":75,"cssClass":"pl-c"}],[],[{"start":12,"end":73,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":20,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":34,"cssClass":"pl-en"},{"start":35,"end":39,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-v"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":81,"cssClass":"pl-s"}],[{"start":0,"end":48,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":59,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-v"},{"start":21,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":32,"cssClass":"pl-v"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":36,"end":45,"cssClass":"pl-s1"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":81,"cssClass":"pl-c"}],[{"start":8,"end":71,"cssClass":"pl-c"}],[],[{"start":8,"end":69,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":20,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":22,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":76,"cssClass":"pl-s"}],[{"start":0,"end":44,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":82,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":83,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-en"},{"start":23,"end":31,"cssClass":"pl-s1"}],[{"start":12,"end":81,"cssClass":"pl-c"}],[{"start":12,"end":33,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":75,"cssClass":"pl-c"}],[],[{"start":12,"end":73,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":85,"cssClass":"pl-c"}],[{"start":12,"end":75,"cssClass":"pl-c"}],[],[],[{"start":12,"end":73,"cssClass":"pl-c"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/girafe-ai/ml-course/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/girafe-ai/ml-course/security/dependabot","repoSecurityAndAnalysisPath":"/girafe-ai/ml-course/settings/security_analysis","repoOwnerIsOrg":true,"currentUserCanAdminRepo":false},"displayName":"k_nearest_neighbor.py","displayUrl":"https://github.com/girafe-ai/ml-course/blob/23f_yandex_ml_trainings/homeworks/assignment01_knn/k_nearest_neighbor.py?raw=true","headerInfo":{"blobSize":"8.08 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"57cc0c6","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fgirafe-ai%2Fml-course%2Fblob%2F23f_yandex_ml_trainings%2Fhomeworks%2Fassignment01_knn%2Fk_nearest_neighbor.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"172","truncatedSloc":"147"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/girafe-ai/ml-course/discussions/new","newIssuePath":"/girafe-ai/ml-course/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/girafe-ai/ml-course/blob/23f_yandex_ml_trainings/homeworks/assignment01_knn/k_nearest_neighbor.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/girafe-ai/ml-course/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/girafe-ai/ml-course/raw/23f_yandex_ml_trainings/homeworks/assignment01_knn/k_nearest_neighbor.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"girafe-ai","repoName":"ml-course","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"KNearestNeighbor","kind":"class","identStart":174,"identEnd":190,"extentStart":168,"extentEnd":8277,"fullyQualifiedName":"KNearestNeighbor","identUtf16":{"start":{"lineNumber":5,"utf16Col":6},"end":{"lineNumber":5,"utf16Col":22}},"extentUtf16":{"start":{"lineNumber":5,"utf16Col":0},"end":{"lineNumber":171,"utf16Col":21}}},{"name":"__init__","kind":"function","identStart":247,"identEnd":255,"extentStart":243,"extentEnd":275,"fullyQualifiedName":"KNearestNeighbor.__init__","identUtf16":{"start":{"lineNumber":8,"utf16Col":8},"end":{"lineNumber":8,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":8,"utf16Col":4},"end":{"lineNumber":9,"utf16Col":12}}},{"name":"fit","kind":"function","identStart":285,"identEnd":288,"extentStart":281,"extentEnd":760,"fullyQualifiedName":"KNearestNeighbor.fit","identUtf16":{"start":{"lineNumber":11,"utf16Col":8},"end":{"lineNumber":11,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":11,"utf16Col":4},"end":{"lineNumber":23,"utf16Col":24}}},{"name":"predict","kind":"function","identStart":770,"identEnd":777,"extentStart":766,"extentEnd":1828,"fullyQualifiedName":"KNearestNeighbor.predict","identUtf16":{"start":{"lineNumber":25,"utf16Col":8},"end":{"lineNumber":25,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":25,"utf16Col":4},"end":{"lineNumber":49,"utf16Col":46}}},{"name":"compute_distances_two_loops","kind":"function","identStart":1838,"identEnd":1865,"extentStart":1834,"extentEnd":3257,"fullyQualifiedName":"KNearestNeighbor.compute_distances_two_loops","identUtf16":{"start":{"lineNumber":51,"utf16Col":8},"end":{"lineNumber":51,"utf16Col":35}},"extentUtf16":{"start":{"lineNumber":51,"utf16Col":4},"end":{"lineNumber":79,"utf16Col":20}}},{"name":"compute_distances_one_loop","kind":"function","identStart":3267,"identEnd":3293,"extentStart":3263,"extentEnd":4364,"fullyQualifiedName":"KNearestNeighbor.compute_distances_one_loop","identUtf16":{"start":{"lineNumber":81,"utf16Col":8},"end":{"lineNumber":81,"utf16Col":34}},"extentUtf16":{"start":{"lineNumber":81,"utf16Col":4},"end":{"lineNumber":101,"utf16Col":20}}},{"name":"compute_distances_no_loops","kind":"function","identStart":4374,"identEnd":4400,"extentStart":4370,"extentEnd":5976,"fullyQualifiedName":"KNearestNeighbor.compute_distances_no_loops","identUtf16":{"start":{"lineNumber":103,"utf16Col":8},"end":{"lineNumber":103,"utf16Col":34}},"extentUtf16":{"start":{"lineNumber":103,"utf16Col":4},"end":{"lineNumber":129,"utf16Col":20}}},{"name":"predict_labels","kind":"function","identStart":5986,"identEnd":6000,"extentStart":5982,"extentEnd":8277,"fullyQualifiedName":"KNearestNeighbor.predict_labels","identUtf16":{"start":{"lineNumber":131,"utf16Col":8},"end":{"lineNumber":131,"utf16Col":22}},"extentUtf16":{"start":{"lineNumber":131,"utf16Col":4},"end":{"lineNumber":171,"utf16Col":21}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/girafe-ai/ml-course/branches":{"post":"JVRJ7mGRmnTtq5fbDLLR2_bhncDw6HbjKa2QMKkAJOsoIs5XD_dXdcuv2uI9yjsSjV8uHJfeQfLHu_yQq1SSBQ"},"/repos/preferences":{"post":"ZWWunfirz7UEk3HbmQk0k3_fSND56pykVeks7gPofiti6wvqOfeMQjbkFvbao7F7tcabkcyVALsmdCfymBBD6g"}}},"title":"ml-course/homeworks/assignment01_knn/k_nearest_neighbor.py at 23f_yandex_ml_trainings · girafe-ai/ml-course"}