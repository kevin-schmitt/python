class Sample:
    """
        class example for sphinx
    """

    def __init__(self, name):
        """
            class constructor

            :param name: Name of object
            :type name: string:

            :return: Object Sample
            :rtype: Sample
        """
        self.name = name

    def displayName(self):
        """
            display name

            :return: None
            :rtype: NoneType
        """
        print(self.name)
        
    def changeName(self, newName):
        """
            change name

            :param newName: new name of parameter name
            :type newName: string:

            :return: Object Sample
            :rtype: Sample
        """
        self.name = newName
