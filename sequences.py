import json

code = """
  create_user -> log_in_on_app
  create_user -> set_sig_on_hoffweb
  create_user -> set_email_on_hoffweb
  create_user -> log_in_on_hoffweb
  set_email_on_hoffweb -> set_sig_on_hoffweb
  set_email_on_hoffweb -> log_in_on_app
  set_email_on_hoffweb -> log_in_on_hoffweb
  set_sig_on_hoffweb -> log_in_on_app
  set_sig_on_hoffweb -> log_in_on_hoffweb
  log_in_on_hoffweb -> accept_EULA
  log_in_on_hoffweb -> reject_EULA
  log_in_on_hoffweb -> log_in_on_app
  reject_EULA -> log_in_on_app
  accept_EULA -> log_in_on_app
  accept_EULA -> set_contact_email
  accept_EULA -> skip_contact_email
  skip_contact_email -> provide_signature
  skip_contact_email -> log_in_on_app
  skip_contact_email -> skip_signature
  set_contact_email -> provide_signature
  set_contact_email -> skip_signature
  skip_signature -> log_in_on_app
  provide_signature -> log_in_on_app
  set_contact_email -> log_in_on_app
  log_in_on_app -> app_reject_EULA
  log_in_on_app -> app_done
  app_reject_EULA -> log_in_on_app
  log_in_on_app -> app_accept_EULA
  app_accept_EULA -> app_set_email
  app_accept_EULA -> app_provide_signature
  app_accept_EULA -> app_skip_signature
  app_accept_EULA -> app_skip_email
  app_set_email -> app_provide_signature
  app_skip_email -> app_provide_signature
  app_set_email -> app_skip_signature
  app_skip_email -> app_skip_signature
  app_skip_signature -> app_done
  app_provide_signature -> app_done
"""

def load_allowed_steps_from_string(string):
  allowed_steps = {}
  lines = [x.strip() for x in string.strip().split('\n')]
  pairs = [x.split(' -> ') for x in lines]
  for key, value in pairs:
    if key not in allowed_steps: allowed_steps[key] = []
    allowed_steps[key].append(value)

  return allowed_steps

allowed_steps = load_allowed_steps_from_string(code)

# print(json.dumps(allowed_steps, indent=True))

def flatten(xxx):
  ret = []
  for xx in xxx:
    for x in xx:
      ret.append(x)
  return ret;

def sequence_has_no_cycles(sequence):
  return len(sequence) == len(list(set(sequence)))

def branch_sequence(sequence):
  old_end = sequence[-1]
  new_ends = allowed_steps.get(old_end, [])
  if new_ends == []: return [sequence]
  new_sequences = [sequence + [x] for x in new_ends]
  return new_sequences

def branch_sequences(sequences):
  new_sequences = flatten([branch_sequence(x) for x in sequences])
  # new_sequences = list(filter(sequence_has_no_cycles, new_sequences))
  return new_sequences

start = "create_user"
finish = "logged_in"

sequences = [[start]]

for x in range(0, 10):
  new_sequences = branch_sequences(sequences);
  sequences = new_sequences

[print(' -> '.join(x)) for x in sequences]

# print(bleh)
