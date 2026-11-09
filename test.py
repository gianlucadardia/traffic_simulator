from helper import *



""" # Example usage
random_number = generate_gaussian_random()
for i in range(10):
    random_number = generate_gaussian_random()
    print(random_number)
 """

""" # Example usage

nodeuuids = load_ref_ids('data/nodeuuid.txt')
rnd_nodeuuids = take_random_nodeuuid(nodeuuids)

# Define the ROTTEN_UUID array

print (ROTTEN_UUID)

# Remove elements in ROTTEN_UUID from rnd_nodeuuids
rnd_nodeuuids = [uuid for uuid in rnd_nodeuuids if uuid not in ROTTEN_UUID]
print (rnd_nodeuuids)
 """
block_ok, block_critical=define_nodeuuids_to_work_with()
