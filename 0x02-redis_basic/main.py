if __name__ == '__main__':
    import redis

    # Create a Redis connection
    r = redis.Redis()

    r.set('name', 'saad')

    print(r.get('name'))

