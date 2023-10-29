def display_chips(chips=None, max_chips=None, max_text_length=None):
    if not chips:
        return ''

    chips = chips[:max_chips] if max_chips else chips
    result = []
    for chip in chips:
        label = chip['label'][:max_text_length] + '...' if max_text_length and len(chip['label']) > max_text_length else chip['label']
        result.append(f'Chip: {label}')

    if max_chips and len(chips) > max_chips:
        result.append(f'...and {len(chips) - max_chips} more items')

    return ', '.join(result)
