Parameter Tuning Guide for Alayssa AI
This guide explains each parameter in your Modelfile and how to adjust them for optimal performance.

🎯 Core Response Parameters
temperature (Default: 0.7)
Controls creativity and randomness

0.1-0.3: Very consistent, factual responses (good for academic topics)
0.4-0.7: Balanced creativity and consistency (recommended for Alayssa)
0.8-1.0: More creative and varied responses (good for casual chat)
dockerfile
PARAMETER temperature 0.7  # Sweet spot for personality + consistency
top_p (Default: 0.9)
Nucleus sampling - controls vocabulary diversity

0.5-0.7: More focused vocabulary
0.8-0.9: Good balance (recommended)
0.95-1.0: Maximum vocabulary diversity
dockerfile
PARAMETER top_p 0.9  # Allows natural language variety
top_k (Default: 40)
Limits word choice to top K options

10-20: Very focused responses
30-50: Good balance (recommended)
100+: Maximum word choice variety
🧠 Memory and Context Parameters
num_ctx (Default: 4096)
Context window size - how much conversation history to remember

2048: Basic memory (shorter conversations)
4096: Extended memory (recommended for Alayssa)
8192: Maximum memory (for very long conversations)
dockerfile
PARAMETER num_ctx 4096  # Remembers longer conversation context
num_predict (Default: 512)
Maximum response length

128: Short responses only
256-512: Good for balanced conversations (recommended)
1024+: Allows very long responses
num_keep (Default: 24)
Tokens to keep from initial prompt

Keeps core personality instructions active
Higher values = more consistent personality
Lower values = more adaptive responses
🚫 Anti-Repetition Parameters
repeat_penalty (Default: 1.1)
Prevents repetitive language

1.0: No penalty (may repeat phrases)
1.05-1.15: Light penalty (recommended)
1.2+: Strong penalty (may affect natural flow)
dockerfile
PARAMETER repeat_penalty 1.1  # Prevents "sis" and "teh" overuse
repeat_last_n (Default: 64)
How many recent tokens to check for repetition

32: Short-term repetition check
64: Good balance (recommended)
128: Long-term repetition check
⚡ Advanced Quality Parameters
mirostat (Default: 2)
Advanced sampling for consistent quality

0: Disabled
1: Mirostat v1
2: Mirostat v2 (recommended for personalities)
mirostat_tau (Default: 5.0)
Target entropy (response quality)

3.0-4.0: More focused responses
5.0: Balanced (recommended)
6.0-8.0: More diverse responses
seed (Default: 42)
Reproducibility seed

Same seed: More consistent personality
-1: Random seed each time
Fixed number: Reproducible responses
🖥️ Performance Parameters
num_thread (Default: 8)
CPU threads to use

Adjust based on your CPU cores
4: Basic performance
8: Good balance
16+: Maximum performance (if you have the cores)
num_gpu (Default: 1)
GPU acceleration

0: CPU only
1: Use GPU if available (recommended)
🎨 Personality Tuning Presets
More Consistent Alayssa
dockerfile
PARAMETER temperature 0.5
PARAMETER top_p 0.8
PARAMETER repeat_penalty 1.15
PARAMETER mirostat_tau 4.0
More Creative Alayssa
dockerfile
PARAMETER temperature 0.8
PARAMETER top_p 0.95
PARAMETER repeat_penalty 1.05
PARAMETER mirostat_tau 6.0
Academic Mode Alayssa
dockerfile
PARAMETER temperature 0.4
PARAMETER top_p 0.7
PARAMETER num_predict 1024
PARAMETER repeat_penalty 1.2
Casual Chat Mode
dockerfile
PARAMETER temperature 0.8
PARAMETER top_p 0.9
PARAMETER num_predict 256
PARAMETER repeat_penalty 1.05
🔧 Testing Your Changes
After modifying parameters:

Recreate the model:
bash
ollama create alayssa-ai -f Modelfile
Test different conversation types:
Casual greetings
Academic discussions
Personal advice requests
Technical topics
Monitor for:
Personality consistency
Response quality
Repetition issues
Response length appropriateness
📊 Parameter Monitoring
Signs You Need to Adjust:
Too Repetitive:

Increase repeat_penalty (1.1 → 1.15)
Increase repeat_last_n (64 → 128)
Too Random/Inconsistent:

Decrease temperature (0.7 → 0.5)
Decrease top_p (0.9 → 0.8)
Responses Too Short:

Increase num_predict (512 → 1024)
Adjust mirostat_tau (5.0 → 6.0)
Responses Too Long:

Decrease num_predict (512 → 256)
Add specific stop tokens
Memory Issues:

Increase num_ctx (4096 → 8192)
Increase num_keep (24 → 48)
🎯 Recommended Starting Configuration
For Alayssa's personality, these parameters work well:

dockerfile
PARAMETER temperature 0.7          # Balanced creativity
PARAMETER top_p 0.9               # Natural vocabulary
PARAMETER top_k 40                # Good word choice variety
PARAMETER repeat_penalty 1.1      # Prevents overuse of "sis/teh"
PARAMETER num_ctx 4096            # Good conversation memory
PARAMETER mirostat 2              # Consistent quality
PARAMETER seed 42                 # Reproducible personality
Start with these and adjust based on your conversations!

