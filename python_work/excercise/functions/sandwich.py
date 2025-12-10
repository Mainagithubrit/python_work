def sandwich_order(*contents):
    print("\nHere is what you ordered in your sandwich:")

    for content in contents:
        print("- {}".format(content.title()))

sandwich_order('chicken', 'cheese', 'tomatoes', 'onions')
sandwich_order('bacon', 'cheese', 'tomatoes', 'lettuce')
sandwich_order('ham', 'tomatoes', 'onions', 'mayonase')
