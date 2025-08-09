
from git_filter_repo import FilterRepo
def replace_secret_key(blob, metadata):
    text = blob.data.decode("utf-8")
    text = text.replace("django-insecure-1ol38w=gw#6203p6phr$9*0=l3lta5+=5-@3k7=r=4wrch+=#h", "")
    # також заміни ключі Stripe, наприклад:
    text = text.replace("sk_test_51RCFf2CBervm4pgommp18lhLdTxzRwqbCJprKiBsT2D9sSlyoLWrBK7N6h0NQ7ntBHu8o0bfHhCkVJxXiyrpsqFL005yR4Vh7I", "")
    text = text.replace("pk_test_51RCFf2CBervm4pgome2T9z4wwK8ZRVqvtkc0Q7yFcHecQeAeqD3OFSNgUM0xCtgImr0ejlRIVkHIhf3YE81vdJR0000EENj89b", "")
    return text.encode("utf-8")

FilterRepo(blob_callback=replace_secret_key).run()
